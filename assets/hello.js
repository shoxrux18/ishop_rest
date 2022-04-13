
// let btn = document.querySelector('button');
// let result = document.querySelector('#result')
// btn.addEventListener("click",function(){
//     result.innerHTML=''
//     fetch("/api/category").then(r=>r.json()).then(r=>{
//         r.categories.forEach(item=>{
//            let d = document.createElement("div")
//            d.innerText = item.name
//            result.append(d)
//         })
//     })
// })

document.querySelector("button").addEventListener('click',function(){
    let data = {
        username: document.querySelector("#login").value,
        password: document.querySelector("#password").value
    }
    alert(JSON.stringify(data))
})

