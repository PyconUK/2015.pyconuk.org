FROM ruby:2.1

RUN mkdir -p /opt/pyconuk/site
WORKDIR /opt/pyconuk/site

RUN apt-get update && \
        apt-get install --yes \
                node

COPY Gemfile /opt/pyconuk/site/
COPY Gemfile.lock /opt/pyconuk/site/
RUN bundle install

EXPOSE 4000

VOLUME /opt/pyconuk/site

CMD ["bundle", "exec", "jekyll", "serve", "--watch", "--host", "0.0.0.0", "--force_polling"]
