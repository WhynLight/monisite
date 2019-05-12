$(document).ready(function(){
    takehosts(hostip,alarmname);
    displaydatas();

    var counter;
    var timer,timer2;
    //点击ip加载60s内对应主机的性能数据图片，并且循环刷新最新的性能数据
    $(".ips").click(function (){
        var getdata = {refre:"",alarm_opt:"",alarm_host:"",last_data:"",take_img:""};
        ipval = $(this).text().trim();
        getdata["refre"] = ipval;
        clearInterval(timer);
        displaydatas(getdata);
        timer = setInterval(displaydatas,2000,getdata);
        //displaydatas(getdata);
        //setTimeout(takeimg,1500);
    });
    
    //为ip对应的主机选择告警阀值方案
    $("select").bind("change",function(){
        var getdata = {refre:"",alarm_opt:"",alarm_host:"",last_data:"",take_img:""};
        getdata["alarm_opt"] = $(this).val();
        getdata["alarm_host"] = this.id;
        saveopt(getdata);
    });

});

//当下拉菜单发生change时将选中告警方案名称保存到数据库
function saveopt(alopt){
    alopt = JSON.stringify(alopt);
    console.log("调用了saveopt");
    console.log(alopt);
    $.ajax({
        url: "",
        type: "GET",
        data: alopt,
        dataType: "json",
        success: function(data,status){}
    });
}

//获取图片
//function takeimg(){
//    $("#cpuimg").attr("src","/static/myall/images/cpu.png"+'?'+Math.random());
//    $("#memimg").attr("src","/static/myall/images/mem.png"+'?'+Math.random());
//    $("#diskimg").attr("src","/static/myall/images/disk.png"+'?'+Math.random());
//}

//function takeimg(){
//    var getdata = {refre:"",alarm_opt:"",alarm_host:"",last_data:"",take_img:"yes"};
//    getdata = JSON.stringify(getdata);
//    $.ajax({
//        url: "",
//        type: "GET",
//        data: getdata,
//        dataType: "json",
//        success: function(data,status){
//            $("#cpuimg").attr("src",data["cpuimg"]);
//            $("#memimg").attr("src",data["memimg"]);
//            $("#diskimg").attr("src",data["diskimg"]);
//        }
//    });
//}

//显示Lastcomm表所有主机ip和阀值配置方案的下拉菜单
function takehosts(hostip,alarmname){
    //显示ip
    for(var i=0;i<hostip.length;i++){
        var showdiv = "<div class='displaybox'>"+
            "<font class='ips' style='float:left;' id=fon"+hostip[i]["host_name"]+">"+hostip[i]["host_ip"]+"&nbsp;&nbsp;</font>"+
            "<form action=''>"+
                "<select id="+String(hostip[i]["host_name"])+">"+
                    //"<option>aaa</option>"+
                "</select>"+
            "</form>"+
            "</div>";
        $("#hosts").append(showdiv);
        var alarm_rule = hostip[i]["alarm_rule"];

        for(var j=0;j<alarmname.length;j++){
            //检测监控数据是否超过阀值
            if (hostip[i]["alarm_rule"]==alarmname[j]["thre_name"]){
                var getdata = {refre:"",alarm_opt:"",alarm_host:"",last_data:"",take_img:""};
                getdata["last_data"] = hostip[i]["host_ip"];
                getdata = JSON.stringify(getdata);
                $.ajax({
                    url: "",
                    type: "GET",
                    data: getdata,
                    dataType: "json",
                    async: false,
                    success: function(data,status){
                        //console.log("alarmname====>"+alarmname);
                        //console.log("j====>"+j);
                        //console.log("alarmname[j]====>"+alarmname[j]);
                        //console.log("alarmname.length====>"+alarmname.length);
                        var condition = data["cpu"]>alarmname[j]["cpu_thre"] || data["mem"]>alarmname[j]["memory_thre"] || data["disk"]>alarmname[j]["disk_thre"];
                        if (condition){
                            $("#fon"+String(hostip[i]["host_name"])).css("color","red");
                        }
                        console.log(condition);
                        console.log("data: "+JSON.stringify(data));
                        console.log("alarmname: "+JSON.stringify(alarmname[j]));
                        console.log("执行了takehosts success()");
                    }
                });
            }
            //创建选择阀值方案的下拉菜单
            if (alarmname[j]["thre_name"]==alarm_rule){
                var confopt = "<option selected='selected'>"+alarmname[j]["thre_name"]+"</option>";
            }
            else {
                var confopt = "<option>"+alarmname[j]["thre_name"]+"</option>";
            }
            var selid = "#"+String(hostip[i]["host_name"]);
            $(selid).append(confopt);
            //$("."+hostip[i]["host_ip"]).html(confopt);
        }
    }
}

//点击ip显示对应主机的监控数据
function displaydatas(iddata){
        console.log("调用了displaydatas()");
        iddata = JSON.stringify(iddata);
        console.log("iddata值为: "+iddata);
        $.ajax({
            url: "",
            type: "GET",
            data: iddata,
            dataType: "json",
            success: function(data,status){
                $("#ipval").text(ipval);
                $("#cpuval").text(data.cpu);
                $("#memval").text(data.mem);
                $("#diskval").text(data.disk);
                console.log("data============>"+JSON.stringify(data));
                $("#cpuimg").attr("src",data["cpuimg"]);
                $("#memimg").attr("src",data["memimg"]);
                $("#diskimg").attr("src",data["diskimg"]);
            }
        });
}

function stopdisplay(){
    clearInterval(referdata);
}
function test(){
    }
