/*function displayDate() {
    alert("dsjklajfdks");
}*/

$(document).ready(function(){

    //将表单提交的阀值数据存入数据库
    $("#subthre").click(function() {
        savethre();
    });

    //将数据库中的阀值配置的数据显示在页面中
    showthre();

    //删除某一条阀值配置数据
    $(".delbut").click(function(){
        var delname = this.id;
        delthre(delname);
    });

});



function showthre(){ 
    thre_val = JSON.parse(thre_val);
    for (var i in thre_val) {
        //document.getElementById("testdemo").innerHTML=thre_val[i]["thre_name"];
        var divstr = "<div class='displaybox father'>"+
            "<div>"+
            "<table width='400px'>"+
            "<tr>"+
            "<td>"+thre_val[i]["thre_name"]+"</td>"+
            "<td>"+thre_val[i]["cpu_thre"]+"</td>"+
            "<td>"+thre_val[i]["disk_thre"]+"</td>"+
            "<td>"+thre_val[i]["memory_thre"]+"</td>"+
            "</tr>"+
            "</table>"+
            "</div>"+
            "<div>"+
            "<button class='delbut'type='button' id="+thre_val[i]["thre_name"]+">删除</button>"+
            "</div>"+
            "</div>";
        $("#threshow").append(divstr);
    }
}

//删除某一条阀值配置数据
function delthre(delname){
        $.ajax({
            url: "delthre",
            type: "POST",
            data: delname,
            //dataType:"json",
            contentType:"application/x-www-form-urlencoded",
            success: function(data,status){
                // alert("数据: \n" + data + "\n状态: " + status);
                 if(status== "success" && data=="success"){
                    alert("删除成功");
                    window.location.reload()
                 }
                 else{
                     alert("删除失败");
                 }
            }
        });
}


function savethre(){
    //提取表单数据并格式化为json字符串
    var thredata = {};
    var formdata = $("#threval").serializeArray();
    $.each(formdata,function() {
        thredata[this.name] = this.value;
    });
    //判断提取后的数据中是否有空值,若有空值则flag为false
    var flag = true;
    for(var key in thredata) {
        if(!thredata[key]) {flag = false;}
    }
    //若数据中心无空值则post给后端
    if(!flag) {
        alert("输入值不能为空");
        return
    } else {
        thredata = JSON.stringify(thredata);
        $.ajax({
            url: "savethre/",
            type: "POST",
            data: thredata,
            //dataType:"json",
            contentType:"application/x-www-form-urlencoded",
            success: function(data,status){
                // alert("数据: \n" + data + "\n状态: " + status);
                 if(status  == "success"){
                    alert("创建成功");
                 } else {
                    alert("创建失败");
                 }
            }
        });
    }
    //阻止form自动提交导致post请求被转为get请求
    event.preventDefault();
    window.event.returnValue = false;
}










