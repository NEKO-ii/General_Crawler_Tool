// GCT DEFAULT SCRIPT FILE (JAVA SCRIPT)
//////////////////////////////////////////////////////////////////

// 变量定义
var data = {};  // 该字典用于存储脚本需要输出的数据

// 函数定义
// 此处编写数据生成逻辑,将生成的数据存储到data字典即可
//////////////////////////////////////////////////////////////////


build = function (a,b) {
    data["result"] = a+b;
}


//////////////////////////////////////////////////////////////////

// 调用函数并输出数据,调用逻辑必须写在run函数中
// 如需要参数,则将参数写在run函数的参数列表
function run(a,b) {
    build(a,b);
    return JSON.stringify(data);
}
