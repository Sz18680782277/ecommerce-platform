# 电商管理系统微服务平台

## 一、项目简介

本项目为一个基于微服务架构的电商管理系统，包含 `user-service`（用户服务）和 `product-service`（商品服务）两个核心子系统。  
服务均采用 FastAPI 开发，支持 Docker 容器化部署，方便快速交付和环境一致。  

项目设计目标是实现一个可扩展、易维护的电商后端基础框架，结合完善的运维监控与自动化 CI/CD 流程，提升开发和运维效率。

---

## 二、系统架构

```

+-----------------------+       +------------------------+
\|      User Service     |       |     Product Service     |
\| (用户认证、管理)       |       | (商品管理、库存控制)    |
+----------+------------+       +-----------+------------+
\|                                |
\|                                |
+-----------Docker Compose-------+
(容器编排管理)
|
+------------------+
\|  Prometheus监控  |
\|  + Grafana面板   |
+------------------+

````

---

## 三、功能特性

- **User Service**  
  - 用户注册、登录（基于 JWT 实现）  
  - 用户信息查询与修改  

- **Product Service**  
  - 商品列表维护  
  - 商品库存查询与管理  

- **基础设施**  
  - 使用 Docker Compose 实现容器化部署  
  - 集成 Prometheus 监控服务健康与性能  
  - Grafana 提供可视化监控面板  

---

## 四、环境及依赖

- 操作系统：Ubuntu 20.04 或更高  
- Docker：20.x 及以上版本  
- Docker Compose：v2.x 版本  
- Python：3.12.x  
- 依赖库见各服务 `requirements.txt` 文件  

---

## 五、快速部署指南

### 1. 克隆项目

```bash
git clone https://github.com/Sz18680782277/ecommerce-platform.git
cd ecommerce-platform
````

### 2. 启动服务

```bash
docker-compose up -d --build
```

* 默认 User Service 监听端口：`8001`
* 默认 Product Service 监听端口：`8002`

### 3. 访问服务接口

* 用户服务 API 示例：`http://localhost:8001/docs`（FastAPI 自动生成接口文档）
* 商品服务 API 示例：`http://localhost:8002/docs`

---

## 六、CI/CD 自动化部署流程

### 触发条件

* 代码推送至 `main` 分支，且修改了 `service/product-service` 目录或 CI 配置文件 `.github/workflows/deploy.yml`

### 流程步骤

1. GitHub Actions 检出代码
2. 利用 Docker Build 构建 `product-service` 镜像
3. 将镜像推送至 Docker Hub 私有仓库
4. 通过 SSH 自动登录远程服务器，执行拉取镜像和重启容器命令

### 关键配置

* GitHub Secrets 中配置：

  * `DOCKER_USERNAME` 和 `DOCKER_PASSWORD`（Docker Hub 账号）
  * `SERVER_IP`（远程服务器 IP）
  * `SSH_PRIVATE_KEY`（无密码 SSH 私钥，用于自动化连接）

### 部署脚本片段（示例）

```bash
cd /root/projects/ecommerce-platform
docker pull frey547/ecommerce-platform-product-service:latest
docker-compose up -d --no-build product-service
```

---

## 七、监控系统说明

* Prometheus 已配置抓取两个微服务的 `/metrics` 端点
* 监控指标包含请求量、错误率、响应时间、容器 CPU 和内存使用率
* Grafana 连接 Prometheus，搭建了专属仪表盘，支持多维度实时监控
* 监控访问地址示例：`http://your-server-ip:3000`

---

## 八、开发规范与项目结构

```
ecommerce-platform/
├── service/
│   ├── user-service/          # 用户服务
│   └── product-service/       # 商品服务
├── .github/workflows/         # GitHub Actions 配置文件
├── docker-compose.yml         # 容器编排配置文件
├── prometheus.yml             # Prometheus 配置文件
└── README.md                  # 项目说明文档
```

* 各微服务采用 FastAPI 编写，目录中包含 `main.py`、`models.py`、`crud.py`、`schemas.py` 等核心模块

---

## 九、后续规划

* 完善订单管理模块，集成支付接口
* 引入 Kubernetes 实现高可用多副本部署

---

## 十、联系方式

* 负责人：施展
* 邮箱：[2383459188@qq.com]
* GitHub 项目地址：[https://github.com/Sz18680782277/ecommerce-platform]

---
