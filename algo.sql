select com_codigo,
com_nombre,
count(*) as cantidad
from dependencia 
inner join comuna
on com_codigo = est_comuna 
where est_dependencia = 1 group by com_nombre
