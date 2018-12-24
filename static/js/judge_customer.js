
function isEmpty(obj){
    if(typeof obj == "undefined" || obj == null || obj == ""){
        return true;
    }else{
        return false;
    }
}

 function isPhoneNum(phone){
     var myreg = /^(((13[0-9]{1})|(15[0-9]{1})|(17[0-9]{1})|(18[0-9]{1}))+\d{8})$/;
     if(!myreg.test(phone))
     {
         return false;
     }
     return true;
 }
function mycustomer(){

    var uname = document.getElementById("cusname").value;
    var utel = document.getElementById("custel").value;
    var uaddress = document.getElementById("cusaddress").value;

    document.getElementById("errormsg").style.display="none";



    if(isEmpty(uname)){
    document.getElementById("errormsg").innerHTML = "name can not be null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }
    if(isEmpty(utel)){
    document.getElementById("errormsg").innerHTML = "telephone can not be null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }
     if(!isPhoneNum(utel)){
    document.getElementById("errormsg").innerHTML = "电话格式不正确";
    document.getElementById("errormsg").style.display="block";
    return false;
    }
    if(isEmpty(uaddress)){
    document.getElementById("errormsg").innerHTML = "address can not be null.";
    document.getElementById("errormsg").style.display="block";
    return false;
    }


    return true;
}