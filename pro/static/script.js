$('.delete').click(function (){
    confirm('delete')
    var now =this
    var id=$(this).attr('pid').toString()
    $.ajax({
        type:'GET',
        url:'/remove',
        data:{
        prod_id:id},
        success:function(data){
            now.parentNode.parentNode.remove()
        }
    })
})