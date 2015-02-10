module Jekyll
  class IPythonNotebook < Converter
    safe true
    priority :low

    def matches(ext)
      ext =~ /^\.ipynbref$/i
    end

    def output_ext(ext)
      ".html"
    end

    def convert(content)
      `ipython nbconvert --config _ipynbs/ipython_nbconvert_config.py --to html --template basic --stdout _ipynbs/#{content}`
    end
  end
end
