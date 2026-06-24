// /secure/event_d.c
#include "/include/ansi.h"

inherit "/std/object";

// 訂閱表結構：([ "event_type": ({ ([ "ob_path": "/daemon/...", "func": "callback" ]) }) ])
private nosave mapping subscriptions;

// 非同步事件佇列
private nosave mixed *event_queue;
private nosave int is_dispatching;

void create() {
    ::create();
    subscriptions = ([]);
    event_queue = ({});
    is_dispatching = 0;
}

// 註冊訂閱
void subscribe(string event_type, string callback_func) {
    object ob = previous_object();
    if (!ob) return;
    
    string ob_path = base_name(ob);
    
    if (!subscriptions[event_type]) {
        subscriptions[event_type] = ({});
    }

    // 避免重複訂閱
    foreach (mapping sub in subscriptions[event_type]) {
        if (sub["ob_path"] == ob_path && sub["func"] == callback_func) {
            return; 
        }
    }

    subscriptions[event_type] += ({ ([
        "ob_path" : ob_path,
        "func"    : callback_func
    ]) });
}

// 取消訂閱
void unsubscribe(string event_type) {
    object ob = previous_object();
    if (!ob || !subscriptions[event_type]) return;

    string ob_path = base_name(ob);
    mapping *new_subs = ({});

    foreach (mapping sub in subscriptions[event_type]) {
        if (sub["ob_path"] != ob_path) {
            new_subs += ({ sub });
        }
    }
    subscriptions[event_type] = new_subs;
}

// 事件分發循環
void dispatch_loop() {
    if (sizeof(event_queue) == 0) {
        is_dispatching = 0;
        return;
    }

    // 取出佇列頭部事件
    mapping event = event_queue[0];
    event_queue = event_queue[1..];

    string event_type = event["event_type"];
    mapping *subs = subscriptions[event_type];

    if (subs && sizeof(subs) > 0) {
        foreach (mapping sub in subs) {
            // 動態載入/尋找訂閱物件
            object target = find_object(sub["ob_path"]);
            if (!target) {
                catch(target = load_object(sub["ob_path"]));
            }

            if (target) {
                // 沙盒隔離，防止單一訂閱者錯誤中斷分發
                mixed err = catch(call_other(target, sub["func"], event));
                if (err) {
                    log_file("event_errors.log", sprintf(
                        "[%s] Event Type: %s Target: %s Error: %s\n",
                        ctime(time()), event_type, sub["ob_path"], to_string(err)
                    ));
                }
            }
        }
    }

    // 繼續分發下一個事件
    if (sizeof(event_queue) > 0) {
        call_out("dispatch_loop", 0);
    } else {
        is_dispatching = 0;
    }
}

// 發布事件
void publish(string event_type, mapping data) {
    mapping event = ([
        "event_id"   : sprintf("%d_%d", time(), random(100000)),
        "event_type" : event_type,
        "timestamp"  : time(),
        "data"       : data
    ]);

    event_queue += ({ event });

    if (!is_dispatching) {
        is_dispatching = 1;
        call_out("dispatch_loop", 0);
    }
}
