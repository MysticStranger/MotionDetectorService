configuration = {
             'darknet_config' : {
                 'configPath' : './darknetlibnew/cfg/yolov4.cfg',
                 'weightPath' : './darknetlibnew/yolov4.weights',
                 'metaPath' : './darknetlibnew/cfg/coco.data',
                 'threshold' : 0.25,
                 'netWidth' : 608,
                 'netHeight' : 608,
             },
             'mmdetection_config' : {
                 'configPath' : './mmdetection/configs/dcn/faster_rcnn_x101_32x4d_fpn_dconv_c3-c5_1x_coco.py',
                 'weightPath' : './mmdetection/checkpoints/faster_rcnn_x101_32x4d_fpn_dconv_c3-c5_1x_coco_20200203-4f85c69c.pth',
             },
             'tracker_config' : {
                 'encoderWeightsPath' : '/home/mysticstranger/devel/SSS.ExPalantir.VideoAnalyticsEngine.Worker/core/main/service/VideoAnalysis/deep_sort_tracker/model_data/mars.pb',
                 'movePercentage' : 0.05,
                 'MOVING_THRESHOLD' : 0.25,
             }
}
