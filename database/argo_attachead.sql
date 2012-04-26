
DROP TABLE IF EXISTS `argo_attachead`;
CREATE TABLE IF NOT EXISTS `argo_attachead` (
    `aid` int(11) unsigned NOT NULL auto_increment,
    `bid` int(11) unsigned NOT NULL,
    `pid` int(11) unsigned NOT NULL,
    `uid` int(11) unsigned NOT NULL,
    `attachidx` varchar(20) NOT NULL,
    
    `filetype` varchar(10),
    `filesize` int(11) unsigned NOT NULL,
    `uploadtime` timestamp NOT NULL default CURRENT_TIMESTAMP,

    PRIMARY KEY (`aid`),
    KEY `attachidx` (`attachidx`)
) ENGINE=MyISAM  DEFAULT CHARSET=GB2312 ;

