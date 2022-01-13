var value_post = {};
function getVal(el) {
	param=el.name;
	val=el.value
	value_post[param]=val;
}

function submit(id_post,id_name,start_time,el_star){
    if (Object.keys(value_post).length<5) {
        alert( 'Оцените пост по всем критериям!' );
    } else {

    value_post["id_post"]=id_post;
    value_post["id_name"]=id_name;
    value_post["start_time"]=start_time[0].textContent;
    $.post( "/postmethod", {
    data: JSON.stringify(value_post)});
    el_star.reset()

    setTimeout(function(){
        location.reload();
   },800);
    }
    }