Name:		eMail
Version:	3.2.3
Release:	1%{?dist}
Summary:	Command line SMTP client
Group:		Applications/Internet
License:	GPLv2+
URL:		https://github.com/guoxiaoqiao/eMail
Source0:	%{name}.tar.bz2

BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:	openssl-devel



%description
Command line SMTP client.


%prep
%setup -q -n %{name}

%build
%configure --with-ssl
make %{?_smp_mflags}

%install 
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/email/*
%{_bindir}/*
%{_mandir}/*
%{_docdir}/*


%changelog
* Tue May 26 2015 小桥 <29551030@qq.com> - 3.2.3
- 初始版本

