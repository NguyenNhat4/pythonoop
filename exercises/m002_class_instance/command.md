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


VEGETABLES (Rau củ) - root vegetables, leafy greens, cruciferous
FRUITS (Trái cây) - berries, tropical fruits, melons
GRAINS_LEGUMES (Ngũ cốc & đậu) - rice, beans, lentils, wheat products
DAIRY_EGGS (Sữa & trứng) - milk products, cheese, eggs
MEAT_SEAFOOD (Thịt & hải sản) - poultry, red meat, fish, shellfish
 