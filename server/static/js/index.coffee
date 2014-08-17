run = ->
    createStoryJS({
        type:       'timeline'
        width:      '100%'
        height:     '600'
        lang:       'zh-cn'
        source:     '/content'
        embed_id:   'my-timeline'
    })

$ ->
  run()