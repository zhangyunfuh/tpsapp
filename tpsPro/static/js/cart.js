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

        // var num1= parseInt($('.numb').val());
        // var detailid=$('#gwc').detailid;

        $.get('/addcart/',{'numb':$('.numb').val(),'detailid':$('#gwc').attr('detailid')},function(response){
            console.log('123')

            if(response.status==0){
				window.open('/login/',target='_self')
			}else{
        		$('.numb').val(response.number);

			}

    	})

    })




})

