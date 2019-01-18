$(function(){
	$('#add').click(function(){
	    var num= parseInt($('.numb').val())+1;
        $('.numb').val(num);
	})
	$('#sub').click(function() {

        var num = parseInt($('.numb').val()) - 1;
        if (num<=0){
            $('.numb').val(0);

        }else{
            $('.numb').val(num);
        }
    })

    $('#gwc').click(function(){
        var num1=$('.numb').val();
        var detailid=$('#gwc').detailid;
        $.get('/addcart/',{'numb':num1,'detailid':detailid},function(response){
        console.log('123')
    })

    })



})

