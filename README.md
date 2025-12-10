# CI/CD Pipeline – GitHub Actions + Docker

Pipeline CI/CD completo que incluye testing automatizado, build de contenedores 
y push a DockerHub. Proyecto ideal para demostrar habilidades DevOps 
y flujo de integración continua.

## 🚀 Funcionalidades
- Tests automáticos con Pytest
- Build optimizado con Docker Buildx
- Push automático a DockerHub
- Estructura profesional de CI/CD
- Pensado para usarse en producción

## 📦 Ejecutar localmente

```
pip install -r requirements.txt
uvicorn app.app:app --reload
```

## 🧪 Correr tests

```
pytest
```

## 🐳 Build Docker

```
docker build -t ci-cd-app .
```

## 👨‍💻 Autor
Carlos Medina  
Solution Architect • Cloud • DevOps • Backend
