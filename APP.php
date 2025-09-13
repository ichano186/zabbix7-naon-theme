<?php

if (version_compare(PHP_VERSION, '8.0.0', '<')) {
        echo sprintf('Minimum required PHP version is %1$s.', '8.0.0');
        exit;
}

require_once dirname(__FILE__).'/ZBase.php';

class APP extends ZBase {
        public static function getThemes() {
                return array_merge(parent::getThemes(), [
                        'naon-theme' => _('Naon Dark')
                ]);
        }
}