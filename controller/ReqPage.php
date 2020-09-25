<?php
namespace app\controller;
use think\facade\Db;

class ReqPage {
    public function getPageMsg($pid = '') {
        // 若传来的是字符串 会进入此分支
        if(!(int)$pid) {
            $return_data = array();
            $return_data['error_code'] = 1;
            $return_data['msg'] = '参数不足: pid';
            return json($return_data);
        } else {
            $data = array();
            $data = Db::table('reqpages')->where('pid', $pid)->select();
            if(sizeof($data) == 0) {
                $return_data['error_code'] = 5;
                $return_data['msg'] = '请求数据不存在';
                return json($return_data);
            } else {
                $return_data['error_code'] = 0;
                $return_data['msg'] = '页面数据请求成功';
                $return_data['data'] = $data;
                return json($return_data);
            }

        }
    }
}

?>