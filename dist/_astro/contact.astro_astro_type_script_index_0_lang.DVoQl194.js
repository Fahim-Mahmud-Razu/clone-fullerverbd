function g(){const d=document.getElementById("vcOpenBtn"),r=document.getElementById("vcCloseBtn"),e=document.getElementById("vcDialog");d&&e&&d.addEventListener("click",()=>{e.showModal()}),r&&e&&r.addEventListener("click",()=>{e.close()}),e&&e.addEventListener("click",a=>{a.target===e&&e.close()});const s=document.getElementById("contactForm"),t=document.getElementById("formStatus");s&&t&&s.addEventListener("submit",a=>{a.preventDefault();const c=document.getElementById("nameInput"),l=document.getElementById("emailInput"),u=document.getElementById("phoneInput"),f=document.getElementById("subjectInput"),p=document.getElementById("commentInput"),n=c?.value.trim()||"",m=l?.value.trim()||"",x=u?.value.trim()||"",o=f?.value.trim()||"",i=p?.value.trim()||"",v=/^[^\s@]+@[^\s@]+\.[^\s@]+$/;if(!n||n.length<2){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> お名前を入力してください。</div>',c?.focus();return}if(!v.test(m)){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 有効なメールアドレスを入力してください。</div>',l?.focus();return}if(!o||o.length<3){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> 件名を入力してください。</div>',f?.focus();return}if(!i||i.length<5){t.innerHTML='<div style="color: #d9534f; background: #fff0f0; border: 1px solid #ffcccc; padding: 12px; border-radius: 4px; font-weight: 600;"><i class="fas fa-exclamation-triangle"></i> お問い合わせ内容を入力してください。</div>',p?.focus();return}const b=`Name: ${n}
Email: ${m}
Phone: ${x||"N/A"}
Subject: ${o}

Message:
${i}

---
Sent via MAX GLOVES BD LTD. Website (Japanese)`,y=`mailto:maxglovesbdltd@gmail.com?subject=${encodeURIComponent(`[Website Inquiry] ${o}`)}&body=${encodeURIComponent(b)}`;t.innerHTML=`
          <div style="background: #f0f7ff; border: 2px solid #05254F; border-radius: 6px; padding: 22px 20px; margin-top: 25px; box-shadow: 0 4px 15px rgba(5,37,79,0.08);">
            <div style="display: flex; align-items: flex-start; gap: 14px;">
              <i class="fas fa-info-circle" style="color: var(--brand-navy); font-size: 24px; margin-top: 2px; flex-shrink: 0;"></i>
              <div>
                <h4 style="color: var(--brand-navy); font-size: 17px; font-weight: 700; margin: 0 0 6px;">
                  ${n}様、お問い合わせをご準備いたしました
                </h4>
                <p style="color: #334155; font-size: 14px; margin: 0 0 14px; line-height: 1.6;">
                  現在、Webフォームは直接お問い合わせモードで運用されています。以下のボタンをクリックしてメールソフトを起動し、営業担当窓口（<strong>maxglovesbdltd@gmail.com</strong>）までお送りいただくか、お電話でお問い合わせください。
                </p>
                <div style="display: flex; flex-wrap: wrap; gap: 12px;">
                  <a href="${y}" class="btn" style="background: var(--brand-orange); color: #ffffff; text-decoration: none; padding: 10px 22px; border-radius: 4px; font-weight: 700; font-size: 14px; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="far fa-envelope"></i> メールソフトで送信
                  </a>
                  <a href="https://wa.me/8801710591088" target="_blank" rel="noopener noreferrer" class="btn" style="background: var(--brand-navy); color: #ffffff; text-decoration: none; padding: 10px 22px; border-radius: 4px; font-weight: 700; font-size: 14px; display: inline-flex; align-items: center; gap: 8px;">
                    <i class="fab fa-whatsapp" style="color: #25D366;"></i> WhatsAppでお問い合わせ (+880 1710-591088)
                  </a>
                </div>
              </div>
            </div>
          </div>
        `})}document.readyState==="loading"?document.addEventListener("DOMContentLoaded",g):g();
