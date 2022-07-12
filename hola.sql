select avg(eva_puntaje_lect),
avg(eva_puntaje_mate), dep_descripcion
from evaluacion 
inner join establecimiento on eva_rbd = est_rbd
where (eva_grado = '6b' or eva_grado = '8b') and eva_agno = '2016'
group by dep_descripcion  
