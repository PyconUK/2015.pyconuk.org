FROM ruby:2.1

MAINTAINER PyConUK Organisers
# Based heavily on grahamc/jekyll

COPY . /pyconuk/
WORKDIR /pyconuk/

RUN apt-get update \
    && apt-get install -y node python-pygments \
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
    && bundle install

EXPOSE 4000

ENTRYPOINT ["bundle", "exec", "jekyll", "serve", "-w"]
