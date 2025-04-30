set -e

while ! nc -z db 5432; do
  echo "🟡 Aguardando iniciar container do Banco de Dados Postgres(db 5432) ..."
  sleep 2
done

echo "✅ Container do Banco de Dados Postgres iniciado com sucesso! (db:5432)"

echo no | python src/manage.py collectstatic --noinput
echo "🟡 Migrando o banco de dados..."
python src/manage.py makemigrations utils authentication lumicore
echo "✅ Migrando o banco de dados com sucesso!"
python src/manage.py migrate --noinput

python src/manage.py shell -c "from authentication.models import Profile; \
                           Profile.objects.filter(username='admin').exists() or \
                           Profile.objects.create_superuser(username='admin',
                           email='admin@example.com', password='123', profileType=1)"

cd /app/src
gunicorn lumicore.wsgi:application --workers=2 --threads=2 --timeout=120 -b 0.0.0.0:8003