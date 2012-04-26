DROP TABLE IF EXISTS `argo_userattr`;
CREATE TABLE IF NOT EXISTS `argo_userattr` (
    `userid` varchar(20) NOT NULL,
    `attr` blob,

     PRIMARY KEY (`userid`)
) ENGINE=MyISAM  DEFAULT CHARSET=GB2312;

