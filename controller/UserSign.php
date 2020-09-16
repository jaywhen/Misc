<?php

namespace app\controller;

use __PHP_Incomplete_Class;
use think\facade\Db;

/*
 * 调用nowcoder随机头图接口
 * 构造随机头图链接
 */
function get_random_head_url() {
    $rdint = random_int(0, 1000);
    $rd_head_url = 'http://images.nowcoder.com/head/' . strval($rdint) . 'm.png';
    return $rd_head_url;
}

class UserSign {
    /*
     * 用户注册
     */
    public function signup() {

        /* 验证用户名是否为空 */
        if (!$_POST['username']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: username';
            return json($return_data);
        }

        /* 验证电话号码是否为空 */
        if (!$_POST['phone_num']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: phone_num';
            return json($return_data);
        }

        /* 验证密码是否为空 */
        if (!$_POST['password']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: password';
            return json($return_data);
        }

        /* 验证重复密码是否为空 */
        if (!$_POST['password_again']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: password_again';
            return json($return_data);
        }

        if ($_POST['password'] != $_POST['password_again']) {
            $return_data = array();
            $return_data['error_code'] = 2 ;
            $return_data['msg'] = '两次输入的密码不一致';
            return json($return_data);
        }

        $where = array();
        $where['phone_num'] = $_POST['phone_num'];
        $user = Db::table('user')->where($where)->find();

        if($user) {
            $return_data = array();
            $return_data['error_code'] = 3;
            $return_data['msg'] = '该手机号已被注册';
            return json($return_data);
        } else {
            $data = array();
            $data['username'] = $_POST['username'];
            $data['password'] = md5($_POST['password']);
            $data['phone_num'] = $_POST['phone_num'];
            $data['head_url'] = get_random_head_url();

            $result = Db::table('user')->insert($data);
            if ($result) {
                $return_data = array();
                $result_data['error_code'] = 0;
                $return_data['msg'] = '注册成功';
                $return_data['data']['user_id'] = Db::table('user')->where('phone_num', $_POST['phone_num'])->value('id');
                $return_data['data']['username'] = $_POST['username'];
                //$return_data['data']['password'] = $_POST['password'];
                $return_data['data']['phone_num'] = $_POST['phone_num'];
                $return_data['data']['head_url'] = $_POST['head_url'];
                return json($return_data);
            } else {
                $return_data = array();
                $return_data['error_data'] = 4;
                $return_data['msg'] = '注册失败';
                return json($return_data);
            }
        }


        dump($_POST);

    }

    /*
     * 用户登录 
     */
    public function signin() {
        if(!$_POST['phone_num']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: password';

            return json($return_data);
        }

        if(!$_POST['password']) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: password';

            return json($return_data);
        }

        // 查询用户
        $user = Db::table('user')->where('phone_num', $_POST['phone_num'])->find();
        if($user) {
            if(md5($_POST['password']) != $user['password']) {
                $return_data = array();
                $return_data['error_code'] = 3;
                $return_data['msg'] = '密码不正确，请重新输入';

                return json($return_data);

            } else {
                $return_data = array();
                $return_data['error_code'] = 0;
                $return_data['msg'] = '登录成功';

                $return_data['data']['user_id'] = $user['id'];
                $return_data['data']['username'] = $user['username'];
                $return_data['data']['phone_num'] = $user['phone_num'];
                $return_data['data']['head_url'] = $user['head_url'];

                return json($return_data);



                 
            }
        } else {
            $return_data = array();
            $return_data['error_code'] = 2;
            $return_data['msg'] = '不存在该手机号用户，请注册';

            return json($return_data);
        }

    }

}

?>