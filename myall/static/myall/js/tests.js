$(document).ready(function(){
    thre_val = JSON.parse(thre_val);
    for (var i in thre_val) {
        //document.getElementById("testdemo").innerHTML=thre_val[i]["thre_name"];
        var divstr = "<div style='display:flex'>"+
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
            "<button type='button' id="+thre_val[i]["thre_name"]+">删除</button>"+
            "</div>"+
            "</div>";
        $("#testdemo").append(divstr);
    }
});

$(document).ready(function(){
    $("button").click(function(){ console.log(this.id)
        
    });
});
