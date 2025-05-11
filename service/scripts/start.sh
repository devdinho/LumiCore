set -e

echo "🟡 Coletando arquivos estáticos: *.js & *.css ..."
echo no | python src/manage.py collectstatic --noinput
echo "✅ Coletando arquivos estáticos com sucesso!"

echo "🟡 Migrando o banco de dados..."
python src/manage.py makemigrations utils authentication lumicore
echo "✅ Migrando o banco de dados com sucesso!"
python src/manage.py migrate --noinput

python src/manage.py shell -c "from authentication.models import Profile; \
                           Profile.objects.filter(username='admin').exists() or \
                           Profile.objects.create_superuser(username='admin',
                           email='admin@example.com', password='123', profileType=1)"

cd /app/src
gunicorn --config gunicorn_config.py lumicore.wsgi:application