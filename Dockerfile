FROM ruby:2.1

MAINTAINER PyConUK Organisers
# Based heavily on grahamc/jekyll

RUN apt-get update \
    && apt-get install -y node python-pygments wget unzip \
    && apt-get clean \
    && gem install \
        bundler \
        html-proofer \
        jekyll \
        jekyll-redirect-from \
        kramdown \
        rdiscount \
        rouge \
        rvm \
    && wget https://github.com/PyconUK/pyconuk.github.io/archive/master.zip \
    && unzip master.zip \
    && rm master.zip \
    && cd pyconuk.github.io-master \
    && bundle install


VOLUME pyconuk.github.io-master
EXPOSE 4000

WORKDIR pyconuk.github.io-master
ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "-w"]
