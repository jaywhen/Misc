<?php

namespace app\controller;

use think\facade\Db;


/*
 * 发布新树洞消息
 */
class Message {
    public function publish() {
        if (!$_POST['user_id']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: user_id';
            return json($return_data);
        }
        if (!$_POST['username']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: username';
            return json($return_data);
        }
        if (!$_POST['head_url']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: head_url';
            return json($return_data);
        }
        if (!$_POST['content']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: content';
            return json($return_data);
        }

        $data = array();
        $data['user_id'] = $_POST['user_id'];
        $data['username'] = $_POST['username'];
        $data['head_url'] = $_POST['head_url'];
        $data['content'] = $_POST['content'];
        $data['total_likes'] = 0;
        $data['send_timestamp'] = date('Y-m-d H:m:s');

        $result = Db::table('message')->insert($data);

        if($result) {
            $return_data = array();
            $return_data['error_code'] = 0;
            $return_data['msg'] = '树洞发布成功';
            return json($return_data);
        } else {
            $return_data = array();
            $return_data['error_code'] = 2;
            $return_data['msg'] = '树洞发布失败';
            return json($return_data); 
        }
        
    }

    /*
     * 获取所有树洞消息
     */
    public function getAllMessages() {
        $all_messages = Db::table('message')->order('send_timestamp desc')->select();
        $return_data = array();
        $return_data['error_code'] = 0;
        $return_data['msg'] = '所有树洞消息获取成功';
        $return_data['data'] = $all_messages;
        return json($return_data);
    }

    /*
     * 获取指定用户的所有树洞消息 
     */
    // public function getUserPublish() {
    //     if(!$_POST['user_id']) {
    //         $return_data = array();
    //         $return_data['error_code'] = 1;
    //         $return_data['msg'] = '参数不足: user_id';
    //         return json($return_data);
    //     } else {
    //         $user = Db::table('message')->where('user_id', $_POST['user_id'])->select();
    //         if($user) {
    //             return json($user);
    //             // $return_data = array();
    //             // $username = $user[1]['username'];
    //             // return $username;
    //             // $return_data['error_code'] = 0;
    //             // $return_data['msg'] = '获取该用户';


    //         } else {
    //             $return_data = array();
    //             $return_data['error_code'] = 2;
    //             $return_data['msg'] = '该用户没有发布任何消息哦';
    //             return json($return_data);
    //         }

    //     }
    // }


}


?>