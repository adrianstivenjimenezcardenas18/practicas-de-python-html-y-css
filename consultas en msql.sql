select id, fecha_publicacion
from post
where year(fecha_publicacion) > '2024';

##########select#
select count(*) as cantidad_de_post
from post;

select * 
##########from#
from usuarios left join post on usuarios.id = post.usuario_id where post.usuario_id is null
union
select *
from usuarios right join post on usuarios.id = post.usuario_id where post.usuario_id is null;

select * 
from post
#######where
where titulo like '%conduccion%' ;

select * 
from post
##############where
where month(fecha_publicacion) = '05';

#############anidando
select *
from post
where usuario_id is not null
and 
estatus = 'activo';

#############group by
select estatus,monthname(fecha_publicacion) as años_post, count(*) as cantida_posrt_por_años
from post
group by años_post, estatus
#############having casi = que el where solo en agrupamiento
having años_post = 'April';


select * 
from post
############order by 
order by fecha_publicacion desc limit 5;

##########cuantas veses cada usuario a creado titulos
select login,count(titulo)as contidad_titulos
from usuarios 
inner join post on usuarios.id =  post.usuario_id
group by login
;


#######cuantas etiquetas tiene este titulo
##############group_concat(nombre_etiqueta) muestra las etiquetas que estan asosiadas a ese pos po scoma sseparadas
select titulo, count(nombre_etiqueta) as num_etiqueta
from post
inner join post_etiquetas on post.id = post_etiquetas.post_id
inner join etiquetas on etiquetas.id = post_etiquetas.etiqueta_id
group by titulo
order by num_etiqueta desc
limit 5
;




