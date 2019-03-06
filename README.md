# SOA

Atsikopijuoti repozitorija:

git clone https://github.com/plssts/SOA

Is SOA/ aplanko subuildinti ir paleisti:

docker-compose up --build -d

Po panaudojimo galima apvalyti <none>:<none> docker atvaizdus:
  
docker rmi $(docker images --filter “dangling=true” -q --no-trunc)
