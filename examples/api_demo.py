#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import json
from rayvision_api.utils import json_load
from rayvision_api import RayvisionAPI

render_para = {
    "domain": "task.renderbus.com",
    "platform": "2",
    "access_id": "xxxxxxx",
    "access_key": "xxxxxxx",
}

api = RayvisionAPI(access_id=render_para['access_id'],
                   access_key=render_para['access_key'],
                   domain=render_para['domain'],
                   platform=render_para['platform'])

# print("======= 获取task_id =============")
# task_id = api.task.task_id

# print("======= 根据task_id提交任务 =============")
# api.submit(task_id=1479581)

# print("======= 根据task_info提交任务 =============")
# task_json_content = json_load(json_path=r"C:\workspace\1590129962\task.json")
# api.submit_by_data(task_info=task_json_content)

# print("======= 根据task_info提交任务 =============")
# json_content = json.dumps(json_load(json_path=r"C:\workspace\1590129962\task.json"))
# api.transmit.upload_json_content(task_id=1479581, content=json_content, file_name="task.json")

# print("======= 获取平台列表 =============")
# platform = api.query.platforms()
# print(platform)
#
# print("======= 获取用户详情 =============")
# user_profile = api.user.query_user_profile()
# print(user_profile)
#
# print("======= 获取用户设置 =============")
# user_setting = api.user.query_user_setting()
# print(user_setting)
#
# print("======= 更新用户设置 =============")
# update_user_setting = api.user.update_user_settings(task_over_time=43200)
# print(update_user_setting)
#
# print("======= 获取用户传输BID =============")
# user_transfer_bid = api.user.get_transfer_bid()
# print(json.dumps(user_transfer_bid, indent=4))
#
# print("======= 创建任务号 =============")
# create_task_id = api.task.create_task(count=1, clone_original_id=1479305)
# print(create_task_id)

# print("======= 提交任务 =============")
# # task_id = create_task_id["taskIdList"][0]
# submit_task = api.task.submit_task(task_id=1479421)
# print(submit_task)

# print("======= 获取分析错误码 =============")
# error_detail = api.query.error_detail(code="675474")
# print(json.dumps(error_detail, indent=4, ensure_ascii=False))
#
# print("======= 获取任务列表 =============")
# task_list = api.query.get_task_list(status_list=[10])
# print(task_list)
#
# print("======= 停止任务 =============")
# stop_task = api.task.stop_task(task_param_list=[1479305])
# print(stop_task)

# print("======= 开始任务 =============")
# start_task = api.task.start_task(task_param_list=[1479305])
# print(start_task)

# print("======= 放弃任务 =============")
# abort_task = api.task.abort_task(task_param_list=[1479305])
# print(abort_task)

# print("======= 删除任务 =============")
# delete_task = api.task.delete_task(task_param_list=[1479305])
# print(delete_task)

# print("======= 获取任务渲染帧详情 =============")
# task_frame = api.query.task_frames(task_id=1479311, page_num=1, page_size=1)
# print(task_frame)

# print("======= 获取任务总渲染帧概况 =============")
# all_frame_status = api.query.all_frame_status()
# print(all_frame_status)

# print("======= 重提失败帧 =============")
# restart_failed_frames = api.query.restart_failed_frames(task_param_list=[1479305])
# print(restart_failed_frames)

# print("======= 重提任务指定帧 =============")
# restart_frame = api.query.restart_frame(task_id=1479307, select_all=1, status=[3])
# print(restart_frame)

# print("======= 获取任务详情 =============")
# task_info = api.query.task_info(task_ids_list=[1479311])
# print(task_info)
#
# print("======= 添加自定义标签 =============")
# add_label_name = api.tag.add_label(new_name="test_tag42", status=0)
# print(add_label_name)

# print("======= 删除自定义标签 =============")
# delete_label_name = api.tag.delete_label(del_name="test_tag4")
# print(delete_label_name)

# print("======= 获取自定义标签 =============")
# label_list = api.tag.get_label_list()
# print(label_list)

# print("======= 获取支持的渲染软件 =============")
# support_software = api.query.supported_software()
# print(support_software)

# print("======= 获取支持的渲染软件插件 =============")
# support_software_plugin = api.query.supported_plugin(name='3ds Max')
# print(support_software_plugin)

# print("======= 新增用户渲染环境配置 =============")
# env = {
#     "cgId": 2000,
#     "cgName": "Maya",
#     "cgVersion": "2020",
#     "renderLayerType": 0,
#     "editName": "testRenderEnv22",
#     "renderSystem": 1,
#     "pluginIds": [1166],
# }
# add_user_env = api.env.add_render_env(data=env)
# print(add_user_env)


# print("======= 修改用户渲染环境配置 =============")
# update_env = {
#     "cgId": 2000,
#     "cgName": "Maya",
#     "cgVersion": "2020",
#     "renderLayerType": 0,
#     "editName": "testRenderEnv20",
#     "renderSystem": 1,
#     "pluginIds": [2703],
# }
# update_user_env = api.env.update_render_env(data=update_env)
# print(update_user_env)

# print("======= 删除用户渲染环境配置 =============")
# delete_user_env = api.env.delete_render_env(edit_name="testRenderEnv21")
# print(delete_user_env)

# print("======= 设置默认渲染环境配置 =============")
# set_default_user_env = api.env.set_default_render_env(edit_name="testRenderEnv7")
# print(set_default_user_env)

# print("======= 获取用户渲染环境配置 =============")
# user_render_config = api.env.get_render_env(name='houdini', os_name=0)
# print(user_render_config)


# print("======= 任务进度图 =============")
# task_processing_img = api.query.get_task_processing_img(task_id=1479225)
# print(task_processing_img)

# print("======= 设置任务超时停止时间 =============")
# set_task_overtime = api.task.set_task_overtime_top(task_id_list=[1479307], overtime=60)
# print(set_task_overtime)


# print("======= 加载缩略图 =============")
# frame_thumbnall = api.query.get_frame_thumbnall(frame_id=107729597)
# print(frame_thumbnall)

# print("======= 获取镭速传输信息 =============")
# transfer_server_msg = api.query.get_transfer_server_msg()
# print(transfer_server_msg)

# print("======= 获取镭速验证key =============")
# raysync_user_key = api.query.get_raysync_user_key()
# print(raysync_user_key)


# print("======= 全速渲染 =============")
# full_speed_render = api.task.full_speed(task_id_list=[1479311])
# print(full_speed_render)


# print("======= 获取传输配置 =============")
# transfer_config = api.transmit.get_transfer_config()
# print(json.dumps(transfer_config, indent=4, ensure_ascii=False))

# print("======= 添加任务标签 =============")
# add_task_tag = api.tag.add_task_tag(task_ids=[1479311], tag="dyt_test")
# print(add_task_tag)


# print("======= 删除任务标签 =============")
# delete_task_tag = api.tag.delete_task_tag(tag_ids=[541, 539])
# print(delete_task_tag)

# print(end - start)

# if __name__ == '__main__':
#     import time
#     import functools32
#
#     @functools32.lru_cache(maxsize=128)
#     def deter_func(x, y):
#         print("5")
#         time.sleep(2)
#
#         return time.time()
#
#     for i in range(100):
#         print(deter_func(1, 2))
#         # deter_func.cache_clear()
#
#     start = time.clock()
#     for i in range(100):
#         print(api.tag.get_project_list(), type(api.tag.get_project_list()))
#         print(api.query.platforms(), type(api.query.platforms()))
#         print(api.task.create_task())
#         api.tag.get_project_list.cache_clear()
#     end = time.clock()