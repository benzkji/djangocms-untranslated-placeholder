from setuptools import setup, find_packages
import os


# not so bad: http://joebergantine.com/blog/2015/jul/17/releasing-package-pypi/
version = __import__('djangocms_untranslated_placeholder').__version__


def read(fname):
    # read the contents of a text file
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="djangocms-untranslated-placeholder",
    version=version,
    url='https://github.com/bnzk/djangocms-untranslated-placeholder',
    license='MIT Licence',
    platforms=['OS Independent'],
    description="djangocms misc",
    long_description=read('PYPI.md'),
    long_description_content_type="text/markdown",
    author=u'Ben Stähli',
    author_email='bnzk@bnzk.ch',
    packages=find_packages(),
    install_requires=(
        'django>=1.8',
        'django-cms>=4.1.0rc1'
    ),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
    ],
)
