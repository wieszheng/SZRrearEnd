FROM python:3.8.10-slim

WORKDIR /szr
COPY . ./szr

# 时区
ENV TZ=Asia/Shanghai
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# 替换源
RUN sed -i s/deb.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list \
    && sed -i s/security.debian.org/mirrors.aliyun.com/g /etc/apt/sources.list \
    && apt-get update \
    && apt-get install -y default-libmysqlclient-dev gcc \
    && apt-get clean

RUN mkdir -p ~/.pip && mkdir -p /etc/supervisor

# pip源
RUN echo "[global]" >> ~/.pip/pip.conf \
    && echo "trusted-host=mirrors.aliyun.com" >> ~/.pip/pip.conf \
    && echo "index-url=http://mirrors.aliyun.com/pypi/simple/" >> ~/.pip/pip.conf \

# 升级pip
RUN python -m pip install --upgrade pip

# supervisor 进程管理
RUN pip install supervisor flask gunicorn
RUN /usr/local/bin/echo_supervisord_conf > /etc/supervisor/supervisord.conf \
    && echo "[include]">>/etc/supervisor/supervisord.conf \
    && echo "files = /etc/supervisor/*.conf">>/etc/supervisor/supervisord.conf

# 拷贝项目进程文件
COPY conf/supervisor.conf /etc/supervisor

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 7777

CMD ["supervisord", "-n","-c", "/etc/supervisor/supervisord.conf"]