function myjudge(){
//    alert("111");
    var name = document.getElementById("name").value;
    var beginTime = document.getElementById("beginTime").value;
    var endTime = document.getElementById("endTime").value;
    var content = document.getElementById("content").value;

    document.getElementById("errormsg").style.display="none";

    if(name.length == 0){
    document.getElementById("errormsg").innerHTML = "name is null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }

    if(beginTime.length == 0){
//     alert("222");
    document.getElementById("errormsg").innerHTML = "beginTime is null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }
    if(endTime.length == 0){
    document.getElementById("errormsg").innerHTML = "endTime is null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }

     if(content.length == 0){
    document.getElementById("errormsg").innerHTML = "content confirm is null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }

    return true;
}

