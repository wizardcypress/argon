/*
    

*/
DROP TABLE IF EXISTS `argo_filehead_${boardname};
CREATE TABLE IF NOT EXISTS `argo_filehead_${boardname}` (
    `pid` int(11) unsigned NOT NULL auto_increment,
    `bid` int(11) unsigned NOT NULL, 
    `filename` varchar(16) NOT NULL,
    `owner` varchar(14),
    `realowner` varchar(14),
    `title` varchar(60),
    `flag` int(11)  unsigned default 0,
    `tid` int(11) unsigned default 0,
    `replyid` int(11) unsigned,
    `posttime` int(11) unsigned, 
    `delflag`  int(11) unsigned NOT NULL default 0,
    `deltime` int(11) unsigned,
    `attachidx` varchar(20),

    `fromaddr` varchar(64),
    `fromhost` varchar(40) NOT NULL,

    `content` text,
    `quote` text,
    `signature` text,
    
    `agree` int(11) ungsigned NOT NULL default 0,
    `disagree` int(11) unsigned NOT NULL default 0,

    PRIMARY KEY (`pid`),
    KEY (`filename`)
) ENGINE=InnoDB  DEFAULT CHARSET=GB2312;


