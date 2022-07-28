function formValidation(){
            
    if(document.forms['searchform']['title'].value== "" && document.forms['searchform']["category"].value=="" && document.forms['searchform']['location'].value=="")
    {
        return false;
    }else{
        return true;
    }
}