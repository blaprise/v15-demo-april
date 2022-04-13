# -*- coding: utf-8 -*-
{
    'name': 'External and Local Videos - eLearning Platform',
    'version': '1.0',
    'summary': 'Manage and publish local and external videos in elearning platform website_slides',
    'category': 'Website/Website',
    'description': """
Insert external videos
======================

Featuring

 * MP4 external videos
 * Livestreaming origin
 * Support Google Drive Videos
 * Support Vimeo Videos
 * Support local uploaded Videos (mp4, ogg and webm)
 * Support embed Zoom Meeting (Updated)
""",
    'author': 'Josue Rodriguez - GAMA Recursos Tecnologicos (PERU)',
    'website': 'https://www.recursostecnologicos.pe',
    'depends': ['website_slides'],
    'data': [
        #'views/loadjs.xml',
        'views/slide_slide.xml',
        'views/res_config_settings.xml',
        'views/qweb.xml',
        'views/template_lesson.xml',
        ],
    'assets': {
        'web.assets_backend': [
        ],
        'web.assets_frontend': [
            '/elearning_external_videos/static/src/js/clappr.min.js',
            'https://player.vimeo.com/api/player.js',
            #'/elearning_external_videos/static/src/js/main_script.js',
            '/elearning_external_videos/static/src/js/slides_course_fullscreen_player.js',
        ],
        'web.assets_tests': [
        ],
        'website.assets_editor': [
        ],
        'website_slides.slide_embed_assets': [
        ],
        'web.qunit_suite_tests': [
        ],
        'web.assets_qweb': [
        ],
        'web.assets_common': [
            '/elearning_external_videos/static/src/css/styles.scss',
        ],
    },
    'demo': [
     ],
    'test': [],
    'images': ['images/main_screenshot.png','images/main_1.png', 'images/main_2.png'],
    'installable': True,
    'auto_install': True,
    'application': True,
    'price': 40.00,
    'currency': 'EUR',
    'license': 'OPL-1',
    'support': 'info@recursostecnologicos.pe',
    #'post_init_hook': 'post_init',
}
