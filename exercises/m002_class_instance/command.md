# tạo và run container 
docker run -d `
  --name mypostgres `
  -e POSTGRES_USER=postgres `
  -e POSTGRES_PASSWORD=Strongpassword1234 `
  -e POSTGRES_DB=shopdb `
  -p 5432:5432 `
  postgres

# truy cập database trong container 

docker exec -it mypostgres psql -U postgres -d shopdb