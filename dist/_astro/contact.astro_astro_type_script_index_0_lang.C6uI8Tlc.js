function g(){const d=document.getElementById("vcOpenBtn"),r=document.getElementById("vcCloseBtn"),e=document.getElementById("vcDialog");d&&e&&d.addEventListener("click",()=>{e.showModal()}),r&&e&&r.addEventListener("click",()=>{e.close()}),e&&e.addEventListener("click",a=>{a.target===e&&e.close()});const c=document.getElementById("contactForm"),t=document.getElementById("formStatus");c&&t&&c.addEventListener("submit",a=>{a.preventDefault();const s=document.getElementById("nameInput"),l=document.getElementById("emailInput"),u=document.getElementById("phoneInput"),f=document.getElementById("subjectInput"),p=document.getElementById("commentInput"),n=s?.value.trim()||"",m=l?.value.trim()||"",x=u?.value.trim()||"",o=f?.value.trim()||"",i=p?.value.trim()||"",v=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;if(!n||n.length<2){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 성함을 입력해 주세요.</div>',s?.focus();return}if(!v.test(m)){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 올바른 이메일 주소를 입력해 주세요.</div>',l?.focus();return}if(!o||o.length<3){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 제목을 입력해 주세요.</div>',f?.focus();return}if(!i||i.length<5){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 문의 내용을 입력해 주세요.</div>',p?.focus();return}const b=`Name: ${n}
Email: ${m}
Phone: ${x||"N/A"}
Subject: ${o}

Message:
${i}

---
Sent via MAX GLOVES BD LTD. Website (Korean)`,y=`mailto:maxglovesbdltd@gmail.com?subject=${encodeURIComponent(`[Website Inquiry] ${o}`)}&body=${encodeURIComponent(b)}`;t.innerHTML=`
          <div style="background: #f0f7ff; border: 2px solid #05254F; border-radius: 6px; padding: 22px 20px; margin-top: 25px; box-shadow: 0 4px 15px rgba(5,37,79,0.08);">
            <div style="display: flex; align-items: flex-start; gap: 14px;">
              <i class="fas fa-info-circle" style="color: var(--brand-navy); font-size: 24px; margin-top: 2px; flex-shrink: 0;"></i>
              <div>
                <h4 style="color: var(--brand-navy); font-size: 17px; font-weight: 700; margin: 0 0 6px;">
                  ${n}님, 문의가 준비되었습니다
                </h4>
                <p style="color: #334155; font-size: 14px; margin: 0 0 14px; line-height: 1.6;">
                  현재 온라인 폼은 직접 문의 모드로 운영되고 있습니다. 아래 버튼을 눌러 이메일 프로그램을 실행하고 영업 담당(<strong>maxglovesbdltd@gmail.com</strong>)으로 직접 발송하시거나 전화로 문의해 주시기 바랍니다.
                </p>
                <div style="display: flex; flex-wrap: wrap; gap: 12px;">
                  <a href="${y}" class="btn" style="background: var(--brand-orange); color: #ffffff; text-decoration: none; padding: 10px 22px; border-radius: 4px; font-weight: 700; font-size: 14px; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="far fa-envelope"></i> 이메일 프로그램으로 발송
                  </a>
                  <a href="https://wa.me/8801710591088" target="_blank" rel="noopener noreferrer" class="btn" style="background: var(--brand-navy); color: #ffffff; text-decoration: none; padding: 10px 22px; border-radius: 4px; font-weight: 700; font-size: 14px; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="fab fa-whatsapp" style="color: #25D366;"></i> WhatsApp 문의 (+880 1710-591088)
                  </a>
                </div>
              </div>
            </div>
          </div>
        `})}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();
