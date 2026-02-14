"""

https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=生活

网址URL的构成：
协议部分：
    https: 加密传输  更安全
    http:  明文传输  内部测试环境 或者 非敏感数据传输

域名部分
    www.baidu.com （World Wide Web） 全球广域网，也称为万维网
    指向 百度 服务器 ip 以及开放的端口

端口
    服务器上的某个程序所允许你访问的端口号
    80 端口 默认  可以不写
    www.baidu.com:80

路径部分
    /s
    作用
        /login   登录
        /reg     注册
        /forget  忘记密码

参数部分
    ?wd=生活
    ?acc=zhangsan&pwd=123&sex=0&age=18
"""