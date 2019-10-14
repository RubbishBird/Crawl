#-*-coding:utf-8-*-

from lxml import etree



text = '''
    <fieldset class="hidden">
        <input type="hidden" name="treeId" value="">
        <input type="hidden" name="treeRequestId" value="/confluence/plugins/pagetree/naturalchildren.action?decorator=none&amp;excerpt=false&amp;sort=position&amp;reverse=false&amp;disableLinks=false">
        <input type="hidden" name="treePageId" value="54427803">

        <input type="hidden" name="noRoot" value="false">
        <input type="hidden" name="rootPageId" value="75469987">

        <input type="hidden" name="rootPage" value="">
        <input type="hidden" name="startDepth" value="0">
        <input type="hidden" name="spaceKey" value="CBDEV" >

        <input type="hidden" name="i18n-pagetree.loading" value="载入中...">
        <input type="hidden" name="i18n-pagetree.error.permission" value="无法载入页面树。看来你没有权限查看根页面。">
        <input type="hidden" name="i18n-pagetree.eeror.general" value="检索页面树时发生问题。有关详细信息，请检查服务器的日志文件。">
        <input type="hidden" name="loginUrl" value="/confluence/login.action?os_destination=%2Fpages%2Fviewpage.action%3FpageId%3D54427803">
        <input type="hidden" name="mobile" value="false">
    </fieldset>
'''

def parse_file():
    parser = etree.HTMLParser(encoding='utf-8')
    # htmlelement = etree.parse('D:\DJworkspace\Crawl\jira.html',parser=parser)
    html = etree.HTML(text)
    print(etree.tostring(html,encoding='utf-8').decode('utf-8'))

if __name__ == '__main__':
    parse_file()