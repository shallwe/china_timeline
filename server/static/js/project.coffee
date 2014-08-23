run = ->
    createStoryJS({
        type:       'timeline'
        width:      '100%'
        height:     '600'
        lang:       'zh-cn'
        source:     '/project_info?project_id=' + project_id
        embed_id:   'timeline-div'
    })

$ ->
  run()