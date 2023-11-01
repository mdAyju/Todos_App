async function api(){
    let res= await fetch('http://127.0.0.1:8000/')
    let data =await res.json()
    console.log(data)

}
api()

let addMob =document.querySelector('.addMob')
let form = document.querySelector('.form-wrapper')
let backBtn= document.querySelector('.backBtn')
let editBtn= document.querySelector('.editBtn')
let deleteBtn =document.querySelector('.deleteBtn')


addMob.onclick=function(){
    form.classList.add('actives')
}
console.log(addMob)

// backBtn.onclick=function(){
//     form.classList.remove('actives')
// }


editBtn.onclick=function(){
    form.classList.add('actives')
}

$('.deleteBtn').click(function(){
    confirm('Want to delete Data')
    let pid= $(this).attr('pid').toString()
    let Now =this
    $.ajax({
        type:'GET',
        url:'http://127.0.0.1:8000/main/',
        data:{
            prod_id:pid
        },

        success:function(data){

            Now.parentNode.parentNode.remove()
        }
    })
})
