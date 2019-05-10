# v2ray-subscriber-web
服务端 自动生成V2ray订阅内容的PHP页面

## 简介
一个PHP页面，内容是可供V2ray订阅的形式（or V2rayN？）  
总之部署上去后，直接把地址加到订阅里面就可以完成订阅的功能  
（会解析出该服务器上所有的V2ray的node）  
  
本项目采用PHP+PYTHON  
PHP非常方便搭建在任何平台上，用PYTHON是为了方便解析出订阅内容  
原本想用PHP写的……我比较懒，就直接上PYTHON了  

## 依赖项
multi-v2ray 一键脚本（我调用的它的PYTHON脚本）
[https://github.com/Jrohy/multi-v2ray](https://github.com/Jrohy/multi-v2ray)

（PHP需要允许shell_exec函数）

