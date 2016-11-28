<?php
/**
 * build dictionary file from README.md
 *
 * ex:
 * cd /path/repo/
 * php bin/mk_dic.php
 */

// 全部用（最後の出力ファイル）
const ALL_DICTIONARY_FILE = 'all/all.dic';

// 個別の入力元であり出力先
const DICTIONARIES_DIRECTORY_NAME = 'dictionaries';

// 入力元ファイル（出力はディレクトリ名.dic固定）
const SRC_FILE_NAME = 'README.md';

// /PATH/TO/REPO/all/all.dic
$all_file = dirname(dirname(__FILE__)) . '/' . ALL_DICTIONARY_FILE;
file_put_contents($all_file, null); // init

// /PATH/TO/REPO/dictionaries
$dictionaries_dir = dirname(dirname(__FILE__)) . '/' . DICTIONARIES_DIRECTORY_NAME;

// list src file. each directories
$src_list = glob($dictionaries_dir . '/*/' . SRC_FILE_NAME);

foreach ($src_list as $src_file) {
    $work_dir = dirname($src_file);
    $work_dir_array = explode('/', $work_dir);
    $work_dir_name = array_pop($work_dir_array);
    // 出力先ファイル名
    $work_dist_file = $work_dir . '/' . $work_dir_name . '.dic';

    $src_contents = file_get_contents($src_file);

    // ## list の後ろからファイル末尾までを取得（ $tmp[1][0] に目的の文字列が入る）
    preg_match_all('/\n\#\# list(.*?)$/sD', $src_contents, $tmp);
    // (行頭の) *, "space(半角空白)", 空行 を除去
    $search = array('*', ' ', "\n\n"); // @memo right?
    $replace = array('', '', '');
    $dist_contents = str_replace($search, $replace, $tmp[1][0]);
    $dist_contents = strtolower($dist_contents);
    // var_dump($dist_contents);

    file_put_contents($work_dist_file, $dist_contents);
    file_put_contents($all_file, $dist_contents, FILE_APPEND);
}
