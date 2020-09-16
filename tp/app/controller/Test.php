<?php
namespace app\controller;

use think\facade\Db;


class Test
{

    public function index() {
        $date = date('Y-m-d H:m:s');
        echo($date);
    }
    // public function test_insert() {
    //     $Message = M('Message');

    //     $data = array();
    //     $data['user_id'] = 1;
    //     $data['username'] = 'jaywhen';
    //     $data['head_url'] = 'http://images.nowcoder.com/head/32m.png';
    //     $data['content'] = 'hello, world!';
    //     $data['send_timestamp'] = time();
    //     $result = $Message->add($data);

    //     var_dump($result);


    // }


    // public function index() {

        //向表中插入数据
        // $data = array();
        // $data['user_id'] = 2;
        // $data['username'] = 'xsun';
        // $data['head_url'] = 'http://images.nowcoder.com/head/64m.png';
        // $data['content'] = 'Hi! php!';
        // $data['send_timestamp'] = time();

        // Db::name('message')->insert($data);

        
    // }
    

}




?>