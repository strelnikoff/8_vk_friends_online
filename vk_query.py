get_online_friends = '\
    var friend = API.friends.get({"fields":"online"});\
    friend = friend.pop();\
    var online = [];\
    var tmp;\
    var n =0;\
    while (tmp = friend.pop()){\
        if (tmp.online==1){\
            n=n+1;\
            online.push(tmp);\
        }\
    }\
    return {"count":n,"items":online};'
