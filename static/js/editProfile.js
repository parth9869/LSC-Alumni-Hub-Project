var educationCard="<div class='row m-2' id='educationSection'><div class='card mb-4 rounded-3 wow slideInUp ' data-wow-delay='0.1s'><div class='card-body wow slideInUp ' data-wow-delay='0.1s'><div class='row m-2'><div class='col-sm-3'> <p class='mb-0'>University Name</p> </div> <div class='col-sm-9'>  <input type='text' name='university[]' class='form-control rounded-3 ' id='university' required /> </div> </div>  <!--university name end--> <!--Degree --> <div class='row m-2'> <div class='col-sm-3'>  <p class='mb-0'>Degree Type</p> </div> <div class='col-sm-9'> <input type='text' name='degree[]' class='form-control rounded-3 ' required /> </div></div><!--Degree end--><!--course -->  <div class='row m-2'>  <div class='col-sm-3'>  <p class='mb-0'>Program Name</p> </div>  <div class='col-sm-9'> <input type='text' name='program[]' class='form-control rounded-3 ' /></div></div> <!--Course end--><!--date-->     <div class='row m-2'> <div class='col-sm-6'>  <p class='mb-0'>Start Date</p> <div class='row ml-2'><input type='date' name='startDate[]' class='form-control rounded-3 '  required /> </div></div><div class='col-sm-6'> <div class='row'><div class='col'> <p class='mb-0'>End Date</p> <div class='row ml-2'> <input type='date' name='endDate[]' class='form-control rounded-3 ' required id='endMonth' /></div></div> </div> <div class='row'>  <div class='col ml-3'>   <input class='form-check-input' type='checkbox' value='' id='educationCheckBox' name='educationCheckBox' /> <label class='form-check-label' for='flexCheckChecked'>Currently attending this university</label> </div> </div> </div>  </div>  <!--date end-->  <!--description--> <div class='row m-2'> <div class='col-sm-3'>  <p class='mb-0'>Description</p> </div>  <div class='col-sm-9'> <textarea name='educationDescription[]' class='form-control rounded-3 ' rows='5' style='white-space: break-spaces;'></textarea> </div> </div> <!--description end--> <div class='row m-1'> <div class='col text-center'><a class='btn bg-secondary text-white' id='deleteEducation'><i class='fa fa-trash-alt m-2'></i>delete</a></div></div><!--eduction section end--></div></div></div>"
$(document).ready(function(){
    var usertype=$(this).find(":selected").text();;
    if (usertype == 'Professor'){
        $("#passingYearDiv").hide();
        $("#programNameDiv").hide();
    }else if(usertype == 'Student'){
        $("#passingYearDiv").hide();
        $("#programNameDiv").show();
    }else{
        $("#passingYearDiv").show();
        $("#programNameDiv").show();
    }
    //following function add education card
    $("#addEduction").click(function(){
        var parent=$(this).parent().parent();
      $(educationCard).insertBefore(parent);
    });

    // following function delete eduction card
    $("body").on('click', "#deleteEducation", function() {
        var parent=$(this).parents("#educationSection");
        $(parent).remove();
        
        
    });

    //following event trigger when check box in education section checked or unchecked
    $("body").on('change', "#educationCheckBox", function() {
        var parentDiv=$(this).parent().parent().parent();
        if(this.checked){
            //if check box is checked, it change type of input filed of end date to text and disable filled
        var month=$(parentDiv).find("#endMonth");
            $(month).attr("type","text");
            $(month).val("Present");
           
            $(month).prop("readonly",true);
            //it disable check box of other sibling eduction cards.
        var eduSection=$(this).parents("#educationSection").siblings("#educationSection").find("#educationCheckBox");
            $(eduSection).prop("disabled",true);
        }else{
            //it reset effect of checked even.
            var month=$(parentDiv).find("#endMonth");
            $(month).attr("type","date");
            
           
            $(month).prop("readonly",false);
        var eduSection=$(this).parents("#educationSection").siblings("#educationSection").find("#educationCheckBox");
            $(eduSection).prop("disabled",false);

        }
        // code here
    });

    // Work experience jquery
    var workDivision='<div class="row m-2" id="workSection"> <div class="card mb-4 rounded-3 wow slideInUp " data-wow-delay="0.1s"> <div class="card-body wow slideInUp " data-wow-delay="0.1s"><!--Position name --><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Position </p></div><div class="col-sm-9"><input type="text" name="position[]" required class="form-control rounded-3 " /></div></div><!--position  end--><!--Company name --><div class="row m-2"><div class="col-sm-3"> <p class="mb-0">Company Name</p></div> <div class="col-sm-9"><input type="text" name="company[]" required class="form-control rounded-3 " /></div></div><!--Company end--><!--date--><div class="row m-2"><div class="col-sm-6"><p class="mb-0">Start Date</p>  <div class="row ml-2"><input type="date" name="startDateWork[]" class="form-control rounded-3 " required /></div></div> <div class="col-sm-6" id="ffr"><div class="row"><div class="col"> <p class="mb-0">End Date</p> <div class="row ml-2"><input type="date" name="endDateWork[]" class="form-control rounded-3 " required id="endMonthWork" /></div></div></div> <div class="row"><div class="col ml-3">   <input class="form-check-input "  type="checkbox" value="" id="workCheckBox" name="workCheckBox" /> <label class="form-check-label" for="flexCheckChecked">Currently work here</label></div> </div></div></div><!--date end--><!--description--><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Description</p> </div> <div class="col-sm-9"> <textarea name="workDescription[]" class="form-control rounded-3 " rows="5" style="white-space: break-spaces;"></textarea></div> </div><!--description end--><div class="row m-1"><div class="col text-center"><a class="btn bg-secondary text-white" id="deleteWork"><i class="fa fa-trash-alt m-2"></i>delete</a> </div></div><!--eduction section end--></div> </div> </div>';

    $("#addWork").click(function(){
        var parent=$(this).parent().parent();
      $(workDivision).insertBefore(parent);
    });

    // following function delete eduction card
    $("body").on('click', "#deleteWork", function() {
        var parent=$(this).parents("#workSection");
        $(parent).remove();
        
        
    });

    $("body").on('change', "#workCheckBox", function() {
        var parentDiv=$(this).parent().parent().parent();
        if(this.checked){
            //if check box is checked, it change type of input filed of end date to text and disable filled
        var month=$(parentDiv).find("#endMonthWork");
            $(month).attr("type","text");
            $(month).attr("value","Present");
            $(month).prop("readonly",true);
            //it disable check box of other sibling eduction cards.
            var workSection=$(this).parents("#workSection").siblings("#workSection").find("#workCheckBox");
            $(workSection).prop("disabled",true);
        }else{
            //it reset effect of checked even.
            var month=$(parentDiv).find("#endMonthWork");
            $(month).attr("type","date");
            $(month).attr("value","1950-05-01");
            
            $(month).prop("readonly",false);
            var workSection=$(this).parents("#workSection").siblings("#workSection").find("#workCheckBox");
            $(workSection).prop("disabled",false);

        }
        // code here
    });

    //publications

    var publicationSection='<div class="row m-2" id="publicationSection"> <div class="card mb-4 rounded-3 wow slideInUp " data-wow-delay="0.1s"><div class="card-body wow slideInUp " data-wow-delay="0.1s"><!--title --><div class="row m-2"><div class="col-sm-3"> <p class="mb-0">Publication Title</p></div><div class="col-sm-9"><input type="text" name="publicationTitle[]" required  class="form-control rounded-3 " /></div></div><!--title  end--><!--journal name --><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Journal Name</p></div><div class="col-sm-9"><input type="text" name="publicationJournal[]" class="form-control rounded-3 " required /></div></div><!--journal end--><!--publication date--><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Date of Publication</p></div><div class="col-sm-9" > <input type="date" name="publicationDate[]" class="form-control rounded-3 " value="1990-05-01" /></div></div><!--publication date end--> <!--publication link--><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Publication URL</p> </div> <div class="col-sm-9"> <input type="url" name="publicationUrl[]" class="form-control rounded-3 "/></div> </div> <!--publication link end--><div class="row m-1"><div class="col text-center"><a class="btn bg-secondary text-white" id="deletePublication"><i class="fa fa-trash-alt m-2"></i>delete</a></div></div><!--eduction section end--></div></div></div>';
    //add new publication section when click on add button
    $("#addPublication").click(function(){
        var parent=$(this).parent().parent();
      $(publicationSection).insertBefore(parent);
    });

    // following function delete eduction card
    $("body").on('click', "#deletePublication", function() {
        var parent=$(this).parents("#publicationSection");
        $(parent).remove();
        
        
    });

    // certification

    var certificationSection='<div class="row m-2" id="certificationSection"><div class="card mb-4 rounded-3 wow slideInUp " data-wow-delay="0.1s"><div class="card-body wow slideInUp " data-wow-delay="0.1s"><!--title --><div class="row m-2"><div class="col-sm-3"><p class="mb-0"> Certificate Title</p> </div><div class="col-sm-9"><input type="text" name="certificateTitle[]" class="form-control rounded-3 " required /> </div></div><!--title  end--><!--Institite name --><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Institute Name</p></div><div class="col-sm-9"> <input type="text" name="certificateInstitute[]" required class="form-control rounded-3 " /></div></div><!--institute end--><!--certification date--><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Issue date</p></div> <div class="col-sm-9" ><input type="date" name="certificateDate[]" class="form-control rounded-3 " value="1990-05-01" /> </div></div><!--certification date end--><!--certification link--><div class="row m-2"><div class="col-sm-3"><p class="mb-0">Credential URL</p></div><div class="col-sm-9"><input type="url" name="certificateUrl[]" class="form-control rounded-3 "/></div></div><!--certification link end--><div class="row m-1"><div class="col text-center"><a class="btn bg-secondary text-white" id="deleteCertificate"><i class="fa fa-trash-alt m-2"></i>delete</a></div></div><!--eduction section end--> </div></div></div>';
    //add new certificate  when click on add button
    $("#addCertificate").click(function(){
        var parent=$(this).parent().parent();
      $(certificationSection).insertBefore(parent);
    });

    // following function delete eduction card
    $("body").on('click', "#deleteCertificate", function() {
        var parent=$(this).parents("#certificationSection");
        $(parent).remove();
        
        
    });

    $("body").on('change',"#userType",function(){

        var usertype=$(this).find(":selected").text();;
        if (usertype == 'Professor'){
            $("#passingYearDiv").hide();
            $("#programNameDiv").hide();
        }else if(usertype == 'Student'){
            $("#passingYearDiv").hide();
            $("#programNameDiv").show();
        }else{
            $("#passingYearDiv").show();
            $("#programNameDiv").show();
        }
    });
    

  });