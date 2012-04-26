/*

    bid: board id, unique
    sid: section id
    boardname: boardname, in English
    description: description of this board
    BM: boardmanager, split by ':' . ie. gcc:cypress
    flag: ?
    level: ?
    post_today: total posts today
    topic_today: total topics today
    lastupdate: last time update board info

*/

DROP TABLE IF EXISTS `argo_boardhead`;
CREATE TABLE IF NOT EXISTS `argo_boardhead` (
    `bid` int(11) unsigned NOT NULL auto_increment,
    `sid` int(11) unsigned NOT NULL,
    `boardname` varchar(20) NOT NULL,
    `description` varchar(50) NOT NULL,
    `BM` varchar(80),
    `flag` int(11) unsigned default 0,
    `level` int(11) unsigned default 0,
    `post_today` int(11) unsigned default 0,
    `topic_today` int(11) unsigned default 0,
    `lastupdate` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP,

    PRIMARY KEY (`bid`),
    KEY `boardname` (`boardname`)
) ENGINE=MyISAM  DEFAULT CHARSET=GB2312 ;

