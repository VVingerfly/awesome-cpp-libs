class LibParser:
    def __init__(self, fp):
        with open(fp, 'r') as f:
            if fp.endswith('.json'):
                import json
                self.libs_info = json.load(f)
            elif fp.endswith('yaml'):
                import yaml
                self.libs_info = yaml.load(f)
            else:
                raise ValueError('Wrong file {}'.format(fp))
            print('Load data from {} done'.format(fp))

    def export_md(self, fp):
        s = self.create_md()
        with open(fp, 'w') as f:
            f.write(s)
        print('Export markdown file to {} done'.format(fp))

    def create_md(self):
        s = self.header()
        s += self.toc()
        s += self.content()
        s += self.footer()
        return s
    
    def export_json(self, fp):
        import json
        with open(fp, 'w') as f:
            json.dump(self.libs_info, f, indent=4)
    
    def export_yaml(self, fp):
        import yaml
        with open(fp, 'w') as f:
            yaml.dump(self.libs_info, f, default_flow_style=False)

    def header(self):
        s = '# Awesome Cpp Libs\n\n' \
        '[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)\n\n' \
        '> An awesome & curated list of cpp libraries for **CV/CGers**.\n\n'
        return s
    
    def footer(self):
        s = '\n## [Back to Top](#table-of-contents)\n'
        return s

    def toc(self):
        toc = '-----\n\n## Table of Contents\n\n'
        for subj in self.libs_info:
            toc += '- [{}](#{})\n'.format(subj, subj.replace(' ', '-').lower())
            for types in self.libs_info[subj]:
                toc += '  - [{}](#{})\n'.format(types, types.replace(' ', '-').lower())
        toc += '\n-----\n'
        return toc
    
    def content(self):
        content = str()
        for subj in self.libs_info:
            print('  ##', subj)
            content += '{} {}\n\n{}'.format('##', subj, self.section(self.libs_info[subj]))
        return content

    def section(self, subjs):
        s = str()
        for subj in subjs:
            print('  ###', subj)
            s += '{} {}\n\n{}'.format('###', subj, self.subsection(subjs[subj]))
        return s

    def subsection(self, subjs):
        s = str()
        for subj in subjs:
            print('  ####', subj)
            s += '{}\n\n'.format(self._get_lib(subjs[subj]))
        return s

    def _get_lib(self, lib):
        name = lib['name']
        repo = lib['repo']
        intro = lib['intro']
        lib_str = '#### {}\n{}\n{}'.format(
            self._md_hlink(name, repo),
            self._md_shield(repo),
            intro)
        return lib_str
    
    def _md_hlink(self, name, url):
        return '[{}]({})'.format(name, url)
    
    def _md_shield(self, repo):
        if not repo.startswith('https://github.com'):
            return str()
        repo_list = repo.split('/', -1)
        repo_user = repo_list[-2]
        repo_name = repo_list[-1]
        # print(repo_user, repo_name)
        watchers = '[![Watchers](https://img.shields.io/github/watchers/{}/{})](Watchers)'.format(repo_user, repo_name)
        stars = '[![Stars](https://img.shields.io/github/stars/{}/{})](Stars)'.format(repo_user, repo_name)
        forks = '[![Forks](https://img.shields.io/github/forks/{}/{})](Forks)'.format(repo_user, repo_name)
        license = '[![License](https://img.shields.io/github/license/{}/{})](LICENSE)'.format(repo_user, repo_name)
        return '{} {} {} {}\n'.format(watchers, stars, forks, license)


if __name__ == "__main__":
    import sys
    args = sys.argv
    if len(args) == 1:
        input = 'awesome-cpp-libs.yaml'
        output = 'README.md'
    elif len(args) == 3:
        input = sys.argv[1]
        output = sys.argv[2]
    else:
        print('Wrong arguments. Usage parser.py in.yaml out.md')
        exit(0)

    print(input, output)
    parser = LibParser(input)
    parser.export_md(output)
